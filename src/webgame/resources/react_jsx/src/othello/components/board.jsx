import React from 'react';
import { Card, Container, Row, Col } from 'react-bootstrap';
import { Square, STONES } from './square.jsx';

export class Board extends React.Component {
    constructor() {
        super();
    }

    createInfoRow(isMyTurn, playerColor, playerUsername, enemyUsername) {
        let nextPlayer = isMyTurn ? playerUsername : enemyUsername;
        let blackStone = <img className="stone-icon" src="/static/images/dog.png"></img>;
        let whiteStone = <img className="stone-icon" src="/static/images/cat.png"></img>;
        if (playerColor == STONES.BLACK) {
            return (
                <Row>
                    <Col xl={9} lg={9} md={9} sm={12} xs={12}>
                        <h6>{playerUsername} {blackStone} vs {whiteStone} {enemyUsername}</h6>
                    </Col>
                    <Col xl={3} lg={3} md={3} sm={12} xs={12}>
                        <h6 clasName="text-right">{nextPlayer}'s Turn</h6>
                    </Col>
                </Row>
            )
        }
        else if (playerColor == STONES.WHITE) {
            return (
                <Row>
                    <Col xl={9} lg={9} md={9} sm={12} xs={12}>
                        <h6>{playerUsername} {whiteStone} vs {blackStone} {enemyUsername}</h6>
                    </Col>
                    <Col xl={3} lg={3} md={3} sm={12} xs={12}>
                        <h6 className="text-right">{nextPlayer}'s Turn</h6>
                    </Col>
                </Row>
            )
        }
        else {
            return (
                <Row>
                <Col xl={12} lg={12} md={12} sm={12} xs={12}>
                    <h6>Click START button to play a game.</h6>
                </Col>
                </Row>
            )
        }
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
        let infoRow = this.createInfoRow(
            this.props.isMyTurn,
            this.props.playerColor,
            this.props.playerUsername,
            this.props.enemyUsername
        );
        let board = this.createBoard(this.props.squares);
        return (
            <Card>
                <Card.Header className="text-center" as="h5">GAME</Card.Header>
                <Card.Body>
                    <Container>
                        {infoRow}
                        <br />
                        {board}
                    </Container>
                </Card.Body>
            </Card>
        );
    }
}