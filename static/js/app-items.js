var Data = React.createClass({
	getInitialState: function(){
		console.log("got initial state");
		return {
			name : '',
			description: ''
		};
	},
	componentDidMount: function(){		
		this.serverRequest = $.get(this.props.source, //+ "2/", 
			function(result){
				var item = result;
				this.setState({
					name: item.name,
					description: item.description
				});
		}.bind(this)
		);
	},
	componentWillUnmount: function(){
		this.serverRequest.abort();
	},
	render: function(){
		return(
			<div>
			<h2>{this.state.name}</h2>
			</div>
		)
	}
});

ReactDOM.render(
	<Data source='http://127.0.0.1:8000/api/'+{{ todo_id }}+'/' />,
	document.getElementById('mountNode')
	)