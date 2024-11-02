import React from "react";
import axios from "axios";



class CustomerProduct extends React.Component{ 
    state = {details: [], }

    componentDidMount() {
    let data;

    axios.get('http://localhost:8000/api/v3/product/')
        .then(res => {
        data = res.data;
        this.setState({
            details: data
        });
        })

        .catch(err => { })
    }

    render(){
    return (
        <div>
            <hr />
        {this.state.details.map((product, id) => (
            <div key={id}>
            <div>
                <h2>{product.name}</h2>
                <h2>{product.price}</h2>
                <h3>{product.description}</h3>
                <h3>{product.image}</h3>
                <h3>{product.available_sizes}</h3>
                <hr /> <hr />
            </div>

        </div>
        ))}
        
        </div>
    
    )
}

};

export default CustomerProduct;