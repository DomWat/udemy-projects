import React, { Component } from 'react'
import BurgerBuilder from './Components/containers/BurgerBuilder'
import Layout from './Components/Layout/Layout.js'

class App extends Component {
  render() {
    return (
      <div>
        <Layout>
          <BurgerBuilder />
        </Layout>
      </div>
    )
  }
}

export default App