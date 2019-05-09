import React from 'react';
import ReactDOM from 'react-dom';
import { Col, Container, Row } from 'react-bootstrap';
import { Board } from './components/board.jsx';
import { STONES } from './components/square.jsx';
import { Chat } from './components/vscpu/chat.jsx';
import { Info } from './components/vscpu/info.jsx';

class App extends React.Component {
    constructor() {
        super();

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

        this.state = {
            squares: squares,
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
                        <Info playerCount={blackCount} cpuCount={whiteCount}/>
                        <br />
                        <Chat />
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