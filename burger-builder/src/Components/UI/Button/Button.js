//not being used delete later if needed


import React from 'react'
import './Button.css'

const button = (props) => (
    <button
        className = {[classes.Button, classes[props.btnType]].join(' ')}
        onClick = {props.clicked}>{props.children}</button>
)

export default button