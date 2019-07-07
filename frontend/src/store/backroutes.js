export default{
	state:{
		baseUrl: 'http://localhost:8000/'
	},
	getters:{
		getLogin(state){
			return state.baseUrl + 'api/auth/jwt/create/'
		}
	}
}