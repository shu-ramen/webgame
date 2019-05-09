import React from 'react';
import ReactDOM from 'react-dom';
import { Col, Container, Row } from 'react-bootstrap';
import { Board } from './components/board.jsx';
import { Info } from './components/vscpu/info.jsx';

class App extends React.Component {
    constructor() {
        super();
    }

    render() {
        return (
            <Container>
                <Row>
                    <Col xl={8} lg={8} md={8} sm={12} xs={12}>
                        <br />
                        <Board />
                    </Col>
                    <Col xl={4} lg={4} md={4} sm={12} xs={12}>
                        <br />
                        <Info />
                    </Col>
                </Row>
            </Container>
        );
    }
}

ReactDOM.render(
    <App />,
    document.getElementById('main')
);