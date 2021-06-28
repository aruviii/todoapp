import Hi from './sample.js';
class Hello extends React.Component {
   render() {
    return (
      <div>
        <Hi/>
      </div>
      );

  }
}

ReactDOM.render(<Hello />, document.getElementById('mydiv'))
