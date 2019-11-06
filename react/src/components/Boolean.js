import React from 'react';
import './Boolean.css';

class Boolean extends React.Component {
  getMode = () => this.props.mode | this.props.mode === 'true';

  buildBackgroundStyle = () => ({
    'backgroundColor': this.getMode() ? "green" : "red",
  })

  render() {
    return (
        <div style={this.buildBackgroundStyle()} className="boolean">
          { this.getMode() ? this.props.trueText : this.props.falseText }
        </div>
    )
  }
}

export default Boolean;