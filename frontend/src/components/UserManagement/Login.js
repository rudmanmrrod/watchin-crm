export default{
  data(){
    return {
      user:{
        username:'',
        password:''
      }
    }
  },
  methods:{
    loginUser(){
      if(this.$validator.validateAll()){
        this.$validator.validate().then( result => {
          if (result){
            this.$axios.post(this.$store.getters.getLogin, this.user)
            .then( response => {
              this.$store.dispatch('login',response.data)
              this.$router.push('/')
            })
            .catch(error => {
              console.log(error)
            })
          }
        })
      }
    }
  }
}