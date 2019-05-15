import React from 'react';
import ReactDOM from 'react-dom';
import request from 'superagent'
import { addHeader } from '../share/csrf.jsx';
import { Col, Container, Row } from 'react-bootstrap';
import { Board } from './components/board.jsx';
import { STONES } from './components/square.jsx';
import { Chat } from './components/vscpu/chat.jsx';
import { Info } from './components/vscpu/info.jsx';

class App extends React.Component {
    constructor() {
        super();

        this.init();

        let squares = [
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1,  0,  1, -1, -1, -1],
            [-1, -1, -1,  1,  0, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1]
        ];

        let isStarted = false;
        if (document.getElementsByName("is-started")[0].value == "True") {
            isStarted = true;
        }
        else {
            isStarted = false;
        }

        this.state = {
            squares: squares,
            initialized: false,
            isMyTurn: false,
            isStarted: isStarted,
            messages: [],
        }

        setInterval(() => this.reload(), 1000);
    }

    init() {

    }

    reload() {
        if (this.state.isStarted) {
            addHeader(request.get("getchat"))
                .end(function (err, res) {
                    if (err) {
                        alert(res.text);
                    }
                    this.setState({
                        messages: res.body["messages"]
                    })
                }.bind(this));
        }
    }

    countStone(squares, stone) {
        let count = 0;
        for (let row of squares) {
            for (let col of row) {
                if (col == stone) {
                    count++;
                }
            }
        }
        return count;
    }

    render() {
        let blackCount = this.countStone(this.state.squares, STONES.BLACK);
        let whiteCount = this.countStone(this.state.squares, STONES.WHITE);

        return (
            <Container fluid>
                <Row>
                    <Col></Col>
                    <Col xl={7} lg={7} md={7} sm={12} xs={12}>
                        <br />
                        <Board squares={this.state.squares}/>
                    </Col>
                    <Col xl={3} lg={3} md={3} sm={12} xs={12}>
                        <br />
                        <Info playerCount={blackCount} cpuCount={whiteCount} isStarted={this.state.isStarted}/>
                        <br />
                        <Chat messages={this.state.messages} isStarted={this.state.isStarted}/>
                    </Col>
                    <Col></Col>
                </Row>
            </Container>
        );
    }
}

ReactDOM.render(
    <App />,
    document.getElementById('main')
);