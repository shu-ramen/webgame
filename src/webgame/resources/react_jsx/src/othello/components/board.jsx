import React from 'react';
import { Card, Container, Row, Col } from 'react-bootstrap';
import { Square } from './square.jsx';

export class Board extends React.Component {
    constructor() {
        super();
    }

    createBoard(squares) {
        let board = squares.slice().map((row) =>
            <Row className="board-row" noGutters>
                <Col></Col>
                <Col></Col>
                {row.slice().map((col) => this.renderSquare(col))}
                <Col></Col>
                <Col></Col>
            </Row>
        )
        return board;
    }

    renderSquare(stone) {
        return (
            <Square stone={stone} />
        );
    }

    render() {
        let board = this.createBoard(this.props.squares);
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
                                <h6>CPU</h6>
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