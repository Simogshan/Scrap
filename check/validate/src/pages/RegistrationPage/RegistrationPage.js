import React from 'react';
//import PropTypes from 'prop-types';
//import { RegistrationPageWrapper } from './RegistrationPage.styled';
import Header from '../../components/header/header';
import Footer from '../../components/footer/footer';
import { useState, useEffect } from 'react';
import axios from 'axios';

const RegistrationPage = () => {
const [phoneNumber, setPhoneNumber] = useState('')

   useEffect ( () => {
      console.log(phoneNumber)
   },[phoneNumber])

   const Register = (event) => {
      axios.post('http://65.0.125.209:8081/number', {
        phoneNumber
    })
      .then(function (response) {
      console.log(response);
      alert (response.data)
    })
      .catch(function (error) {
      console.log(error);
    });
    event.preventDefault()
  }

   return (

      <div>
         <Header />

         <form onSubmit = {Register}>
            <label>Mobile Number</label>
            <input type = 'text' value = {phoneNumber} onChange = {(event) => setPhoneNumber(event.target.value)} placeholder = 'Enter Mobile Number' />
            <br />
            <button>Register</button>
         </form>

         <Footer />

      </div>


   );
}


//RegistrationPage.propTypes = {};

//RegistrationPage.defaultProps = {};

export default RegistrationPage;
