import React from 'react';
import { Row, Col } from 'react-bootstrap';
import { Square } from './square.jsx';

export class Board extends React.Component {
    constructor() {
        super();
    }

    createBoard(squares) {
        let board = squares.slice().map((row) =>
            <Row bsPrefix="row board-row" noGutters>
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
            <div>
                {board}
            </div>
        );
    }
}