export default{
  data(){
    return {
      user:{
        email:'',
        password:''
      }
    }
  },
  methods:{
    loginUser(){
      if(this.$validator.validateAll()){
        this.$validator.validate().then( result => {
          if (result){
            console.log("valid!")
          }
        })
      }
    }
  }
}