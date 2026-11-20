import sys

# Display existing module search paths
print("Original paths:")
for path in sys.path:
    print(path)

# Add the TRIGNOMETRY folder
sys.path.append(r"D:\Learnings\Python Projects AI\TRIGNOMETRY")

# Display updated paths
print("\nUpdated paths:")
for path in sys.path:
    print(path)

# Import your custom module
import Trignometry

print("\nsin(30):", Trignometry.sine(30))
print("cos(60):", Trignometry.cosine(60))
print("tan(45):", Trignometry.tangent(45))