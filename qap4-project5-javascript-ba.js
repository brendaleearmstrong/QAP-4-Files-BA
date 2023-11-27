// FileName:qap4-project5-javascript-ba.js
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
const MotelCustomer = {
  // Main properties
  name: "Brenda Armstrong",
  birthDate: "1979-10-25",
  gender: "Female",
  roomPreferences: ["King", "Non-smoking", "Jacuzzi", "Wine with Cheese Package", "Pet-friendly"],
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

  // Method to calculate age
  calculateAge: function () {
    const today = new Date();
    const birthYear = new Date(this.birthDate).getFullYear();
    const currentYear = today.getFullYear();
    return currentYear - birthYear;
  },

  // Method to calculate stay duration
  calculateStayDuration: function () {
    const oneDay = 24 * 60 * 60 * 1000;
    const checkInDate = new Date(this.checkInAndOutDates.checkIn);
    const checkOutDate = new Date(this.checkInAndOutDates.checkOut);
    return Math.round(Math.abs((checkInDate - checkOutDate) / oneDay));
  },
};

// Create a template literal string
const html = `
  Name: ${MotelCustomer.name}
  Address: ${MotelCustomer.mailingAddress.streetAddress}, ${MotelCustomer.mailingAddress.city}, ${MotelCustomer.mailingAddress.province}, ${MotelCustomer.mailingAddress.postalCode}
  Age: ${MotelCustomer.calculateAge()}
  Gender: ${MotelCustomer.gender}
  Room Preferences: ${MotelCustomer.roomPreferences.join(', ')}
  Payment Method: ${MotelCustomer.paymentMethod}
  Phone Number: ${MotelCustomer.phoneNumber}
  Check-in Date: ${MotelCustomer.checkInAndOutDates.checkIn}
  Check-out Date: ${MotelCustomer.checkInAndOutDates.checkOut}
  Stay Duration: ${MotelCustomer.calculateStayDuration()} days
`;

// Log the HTML to the console
console.log(html);
