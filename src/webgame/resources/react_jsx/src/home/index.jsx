import React from 'react'
import ReactDOM from 'react-dom'
import request from 'superagent'

function addHeader(request, csrfToken) {
    return request
      .set('X-CSRFToken', csrfToken)
      .set('X-Requested-With', 'XMLHttpRequest');
}

class Home extends React.Component {
    constructor() {
        super();
        this.state = {
            count: 0,
        }
    }

    countUp() {
        this.setState({
            count: (this.state.count + 1),
        });
    }

    sendData() {
        var url = '/send_data';

        var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

        addHeader(request.post(url), csrfToken)
            .send({
                data: "data",
            })
            .end(function(err, res){
                if (err) {
                  alert(res.text);
                }
                alert(res.text);
            }.bind(this));
    }

    render() {
        return (
            <div className="home">
                <a href="#" onClick={() => this.countUp()}>{this.state.count}</a><br></br>
                <a href="#" onClick={() => this.sendData()}>Send Data</a>
            </div>
        );
    }
}

ReactDOM.render(
    <Home />,
    document.getElementById('root')
);