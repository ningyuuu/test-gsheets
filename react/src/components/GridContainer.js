import React from 'react';
import EmptyGridObject from './EmptyGridObject';

import './GridContainer.css';
import logo from '../logo.svg';

class GridContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      rows: 1,
      columns: 3,
    }
  }

  componentDidMount() {
    const grid = []
    for (let i = 0; i < this.state.rows; i++) {
      grid.push(new Array(this.state.columns).fill(null));
    }
    
    grid[0][1] = <img src={logo} className="App-logo" alt="logo" />;

    this.setState({ grid });
    console.log('grid loaded!');
  }


  generateGridStyle = () => ({
    gridTemplateRows: `repeat(${this.state.rows}, 1fr)`,
    gridTemplateColumns: `repeat(${this.state.columns}, 1fr)`
  });

  generateGrid = () => {
    if (!this.state.grid) {
      return null;
    }

    const grid = this.state.grid.map(row => (
      row.map(cell => cell || <EmptyGridObject />)
    ));

    return grid;
  }

  render() {
    const grid = this.generateGrid();
    return (
      <div className="maingrid" style={this.generateGridStyle()}>
        {grid}
      </div>
    );
  }
}

export default GridContainer;