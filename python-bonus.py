#Filename: python-bonus.py
#Description: Bonus Graph Program
#Author: Brenda Armstrong, SD10

#Imports
import matplotlib.pyplot as plt

#Inputs
JanClaim = input("Enter the claim amount for January: ")
FebClaim = input("Enter the claim about for February: ")
MarClaim = input("Enter the claim amount for March : ")
AprilClaim = input("Enter the claim amount for April: ")
MayClaim = input("Enter the claim amount for May: ")
JuneClaim = input("Enter the claim amount for June: ")
JulyClaim = input("Enter the claim amount for July: ")
AugClaim = input("Enter the claim amount for Aug: ")
SeptClaim = input("Enter the claim amount for Sept: ")
OctClaim = input("Enter the claim amount for Oct: ")
NovClaim = input ("Enter the claim amount for Nov: ")
DecClaim = input("Enter the claim amount for Dec: ")

#Graph
x_axis = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
y_axis = [float(JanClaim), float(FebClaim), float(MarClaim), float(AprilClaim), float(MayClaim), float(JuneClaim), float(JulyClaim), float(AugClaim), float(SeptClaim), float(OctClaim), float(NovClaim), float(DecClaim)]

plt.title("Customer Claims by Month")
plt.scatter(x_axis, y_axis, color='blue', marker='x', label="Dollar amount")

plt.xlabel("Month")
plt.ylabel("Claim Amount")

plt.grid(True)
plt.legend()

plt.show()
