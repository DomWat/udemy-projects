import React, { Component } from 'react'
import Button from '../../../UI//Button/Button'
import classes from './ContactData.module.css'

class ContactData extends Component {
    state = {
        name: '',
        email: '',
        address: {
            street: '',
            zip: ''
        }
    }

    render() {
        return(
            <div className = {classes.ContactData}>
                <h4>Enter your Contact Data</h4>
                <form>
                    <input className = {classes.Input} type = 'text' name = 'name' placeholder = 'Your name' />
                    <input className = {classes.Input} type = 'email' name = 'email' placeholder = 'Your email' />
                    <input className = {classes.Input} type = 'text' name = 'street' placeholder = 'Your street name' />
                    <input className = {classes.Input} type = 'text' name = 'zip' placeholder = 'Your zip' />
                    <Button btnType = 'Success'>ORDER</Button>
                </form>
            </div>
        )
    }
}


export default ContactData