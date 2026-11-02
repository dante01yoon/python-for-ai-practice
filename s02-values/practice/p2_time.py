total = int(input("Seconds: "))
hours = total // 3600
minutes = total % 3600 // 60
seconds = total % 60
print(f"{hours} h {minutes} min {seconds} s")
