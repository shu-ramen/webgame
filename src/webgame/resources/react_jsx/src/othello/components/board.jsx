import React from 'react';
import request from 'superagent'
import { addHeader } from '../../share/csrf.jsx';
import { Card, Container, Row, Col } from 'react-bootstrap';
import { Square } from './square.jsx';

export class Board extends React.Component {
    constructor() {
        super();
    }

    createBoard(squares) {
        let board = squares.slice().map((row, y) =>
            <Row className="board-row" noGutters>
                <Col></Col>
                <Col></Col>
                {row.slice().map((col, x) => this.renderSquare(col, x, y))}
                <Col></Col>
                <Col></Col>
            </Row>
        )
        return board;
    }

    renderSquare(stone, x, y) {
        if (this.props.isMyTurn == true) {
            return (
                <Square stone={stone} onClick={() => this.props.putStone(x, y)} />
            );
        }
        else {
            return (
                <Square stone={stone} onClick={() => alert("It is not your turn!")}/>
            );
        }
    }

    render() {
        let board = this.createBoard(this.props.squares);
        let nextPlayer = this.props.isMyTurn == true ? "YOU" : "CPU";
        return (
            <Card>
                <Card.Header className="text-center" as="h5">GAME</Card.Header>
                <Card.Body>
                    <Container>
                        <Row>
                            <Col xl={7} lg={7} md={7} sm={12} xs={12}>
                                <h6>Player vs CPU</h6>
                            </Col>
                            <Col xl={3} lg={3} md={3} sm={12} xs={12}>
                                <h6>Next Player</h6>
                            </Col>
                            <Col xl={2} lg={2} md={2} sm={12} xs={12}>
                                <h6>{nextPlayer}</h6>
                            </Col>
                        </Row>
                        <br />
                        {board}
                    </Container>
                </Card.Body>
            </Card>
        );
    }
}