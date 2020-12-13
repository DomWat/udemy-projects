import React, { Component } from 'react'
import Button from '../../../UI//Button/Button'
import classes from './ContactData.module.css'
import axios from '../../../../axios-orders'
import Spinner from '../../../UI/Spinner/Spinner'

class ContactData extends Component {
    state = {
        name: '',
        email: '',
        address: {
            street: '',
            zip: ''
        },
        loading: false
    }

    orderHandler = (event) => {
        event.preventDefault()
        this.setState({ loading: true })
        const order = {
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
                this.props.history.push('/')
            })
            .catch(error => {
                this.setState({ loading: false })
            })
    }

    render() {
        let form = (
            <form>
                <input className={classes.Input} type='text' name='name' placeholder='Your name' />
                <input className={classes.Input} type='email' name='email' placeholder='Your email' />
                <input className={classes.Input} type='text' name='street' placeholder='Your street name' />
                <input className={classes.Input} type='text' name='zip' placeholder='Your zip' />
                <Button btnType='Success' clicked={this.orderHandler}>ORDER</Button>
            </form>)
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