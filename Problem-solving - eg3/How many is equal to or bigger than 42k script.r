data1 <- read.csv("csv", header = TRUE)

# Function to check if the sum of two elements is >= 42
is_sum_ge_42 <- function(q, r, s, w, x, y, z) {
  return (q + r + s + w + x + y + z + 24630 >= 42000)
}

# Initialise a counter for combinations >= 42k
combinations_ge_42  <- 0

# Loop through the combinations of elements
for (i in 1:13) {
  for (j in 14:16) {
    for (k in 17:23) {
        for (l in 24:27){
            for (m in 28:36){
                for(n in 37:45){
                    for(o in 46:47){
                        if (is_sum_ge_42(data1[i, 3], data1[j, 3], data1[k, 3], data1[l, 3], data1[m, 3], data1[n, 3], data1[o, 3])) {
      combinations_ge_42  <- combinations_ge_42 + 1
    }
                    }
                }
            }
        }
    }  
  }
}

