library(readr)
library(dplyr)
library(tidyr)

path <- "C:/Users/choiy/Documents/GitHub/miscellaneous/Automating data manipulation eg1/Before"
setwd(path)
# List all CSV files
csv_files <- list.files(pattern = "\\.csv$")

# Loop over each file
for (file_name in csv_files) {
    # Construct a new file path for the output
    output_file <- paste0(path,"/test/", gsub(", ", "_", gsub(".csv", "", file_name)), "_done.csv")
    
    # Read the CSV file
    data <- read_csv(file_name, col_names = TRUE)
    
    # Rename columns
    data <- data %>%
            rename(workforce_margin_error = "Workforce by Occupation and Gender Moe",
                   number_workforce = "Workforce by Occupation and Gender") %>%
            select(Occupation, number_workforce)
    
    # Identify duplicates
    dup <- data[duplicated(data$Occupation) | duplicated(data$Occupation, fromLast = TRUE), ]
    dup[["sum"]] <- NA
    
    # Calculate the sum for duplicates
    for(i in 1:nrow(dup)){
        dup[["sum"]][i] <- sum((data %>% filter(Occupation == dup[["Occupation"]][i]))[["number_workforce"]])
    }
    
    # Process duplicate data
    dup <- dup %>%
          select(Occupation, sum) %>%
          distinct(Occupation, .keep_all = TRUE)
    
    # Update main data frame
    data <- data %>%
            distinct(Occupation, .keep_all = TRUE) %>%
            left_join(dup, by = "Occupation")
    
    data$number_workforce <- ifelse(is.na(data$sum), data$number_workforce, data$sum)
    data <- select(data, -sum)
    
    # Save the modified CSV
    write.csv(data, output_file, row.names = FALSE)
}
