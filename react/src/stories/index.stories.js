import React from 'react';
import Boolean from '../components/Boolean.js';

export default { title: 'Boolean' };

export const booleanTrue = () => <Boolean mode="true" />;
export const booleanFalse = () => <Boolean mode="false" />;

export const smallBoolean = () => (
  <div style={{ 'width': '100px', 'height': '100px' }}>
    <Boolean mode="true" trueText="true" falseText="false" />
  </div>
);

class ToggleBoolean extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      mode: true
    }
  }

  toggleMode = () => {
    this.setState({
      mode: !this.state.mode
    })
  };

  render() {
    return (
      <div onClick={this.toggleMode}>
        <Boolean mode={this.state.mode} {...this.props} />
      </div>
    )
  }
}

export const toggleBoolean = () => <ToggleBoolean trueText="click to toggle" falseText="click to toggle" />