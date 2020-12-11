import React, { Component } from 'react'
import BurgerBuilder from './Components/containers/BurgerBuilder'
import Layout from './Components/Layout/Layout.js'
import Checkout from './Components/containers/Checkout/Checkout'

class App extends Component {
  render() {
    return (
      <div>
        <Layout>
          <BurgerBuilder />
          <Checkout />
        </Layout>
      </div>
    )
  }
}

export default App