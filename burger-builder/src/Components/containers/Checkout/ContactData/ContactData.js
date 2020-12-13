import React, { Component } from 'react'

import button from '../../../UI/Button/Button.module.css'
import classes from './ContactData.module.css'
import axios from '../../../../axios-orders'
import Spinner from '../../../UI/Spinner/Spinner'

class ContactData extends Component {
    state = {
        name: '',
        email: '',
        address: {
            street: '',
            zip: '',
        },
        loading: false
    }

    orderHandler = (event) => {
        event.preventDefault()
        this.setState({ loading: true })
        // uses the baseURL created in axios-orders + '/orders.json' and sends to firebase
        // .json is required by firebase
        // this is a POST
        const order = {
            // this creates the order that will be sent to DB
            ingredients: this.props.ingredients,
            price: this.props.price,
            customer: {
                name: 'Dom Waters',
                address: {
                    street: 'Teststreet 1',
                    city: 'Houston',
                    state: 'Texas'
                },
                email: 'test@test.com'
            },
            deliveryMethod: 'fastest'
        }
        axios.post('/orders.json', order)
            .then(response => {
                this.setState({ loading: false })
            })
            .catch(error => {
                this.setState({ loading: false })
            })
    }

    render() {
        let form = (
            <form>
                <input className={classes.Input} type='text' name='name' placeholder='Your Name' />
                <input className={classes.Input} type='email' name='email' placeholder='Your Email' />
                <input className={classes.Input} type='text' name='street' placeholder='Your Street Name' />
                <input className={classes.Input} type='text' name='zip' placeholder='Your Zip' />
                <button className={button.Success} onClick={this.orderHandler}>Order</button>
            </form>
        )
        if (this.state.loading) {
            form = <Spinner />
        }
        return (
            <div className={classes.ContactData}>
                <h4>Enter your Contact Data</h4>
                {form}
            </div>
        )
    }
}

export default ContactData