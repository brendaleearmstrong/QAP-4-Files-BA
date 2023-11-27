// FileName: motelCustomer.js
// QAP 4 - JavaScript
/*
  Motel Customer Information

  This script defines a MotelCustomer object with properties and methods
  to represent a customer staying at a motel. The customer information is
  then used to generate a descriptive HTML string.

  Author: Brenda Armstrong
  Date: Monday, November 27, 2023
*/

// Define a MotelCustomer object
const motelCustomer = {
  // Main properties
  name: "Brenda Armstrong",
  birthDate: "1979-10-25",
  gender: "Female",
  roomPreferences: ["king", "non-smoking", "jacuzzi", "wine", "pet-friendly"],
  paymentMethod: "Credit Card",
  
  // Sub-object for mailing address
  mailingAddress: {
    streetAddress: "67 Springdale Street",
    city: "St. John's",
    province: "NL",
    postalCode: "A1C 5B3",
  },

  phoneNumber: "709-682-6878",
  
  // Sub-object for check-in and check-out dates
  checkInAndOutDates: {
    checkIn: "2023-10-31",
    checkOut: "2023-11-07",
  },

  // Function to calculate age
  calculateAge: function () {
    const today = new Date();
    const birthYear = new Date(this.birthDate).getFullYear();
    const currentYear = today.getFullYear();
    return currentYear - birthYear;
  },

  // Function to calculate stay duration
  calculateStayDuration: function () {
    const oneDay = 24 * 60 * 60 * 1000;
    const checkInDate = new Date(this.checkInAndOutDates.checkIn);
    const checkOutDate = new Date(this.checkInAndOutDates.checkOut);
    return Math.round(Math.abs((checkInDate - checkOutDate) / oneDay));
  },

  // Method to generate a customer description as a template literal string
  generateCustomerDescription: function () {
    return `
      <p><strong>Name:</strong> ${this.name}</p>
      <p><strong>Address:</strong> ${this.mailingAddress.streetAddress}, ${this.mailingAddress.city}, ${this.mailingAddress.province}, ${this.mailingAddress.postalCode}</p>
      <p><strong>Age:</strong> ${this.calculateAge()}</p>
      <p><strong>Gender:</strong> ${this.gender}</p>
      <p><strong>Room Preferences:</strong> ${this.roomPreferences.join(', ')}</p>
      <p><strong>Payment Method:</strong> ${this.paymentMethod}</p>
      <p><strong>Phone Number:</strong> ${this.phoneNumber}</p>
      <p><strong>Check-in Date:</strong> ${this.checkInAndOutDates.checkIn}</p>
      <p><strong>Check-out Date:</strong> ${this.checkInAndOutDates.checkOut}</p>
      <p><strong>Stay Duration:</strong> ${this.calculateStayDuration()} days</p>
    `;
  },
};

const customerDescription = motelCustomer.generateCustomerDescription();
console.log(customerDescription);
