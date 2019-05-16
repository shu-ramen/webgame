import React from 'react';
import { Col } from 'react-bootstrap';

export const STONES = {
    NONE: -1,
    BLACK: 0,
    WHITE: 1,
}

export class Square extends React.Component {
    constructor() {
        super();
    }

    getStoneTag(stone) {
        if (stone == STONES.BLACK) {
            return (
                <img className="stone" src="/static/images/dog.png"></img>
            )
        }
        else if (stone == STONES.WHITE) {
            return (
                <img className="stone" src="/static/images/cat.png"></img>
            )
        }
        else {
            return ""
        }
    }

    render() {
        let stoneTag = this.getStoneTag(this.props.stone);
        return (
            <Col className="square-col">
                <button className="square" onClick={() => this.props.onClick()}>
                    {stoneTag}
                </button>
            </Col>
        );
    }
}