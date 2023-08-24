export default { 
    showSnackbar(msg, options={delay: 5000}) {
      var snackbar = document.getElementById("snackbar-container")
      var message = document.getElementById("snackbar-message")
      
      // Show snackbar
      snackbar.style.display = "block";
  
      // Add message
      message.innerHTML = msg
  
      // Hide after delay
      if(typeof options === 'object' && 'delay' in options && options.delay > 0){
        setTimeout(() => {
          this.hideSnackbar()
        }, options.delay)
      }
    },
    hideSnackbar() {
      var snackbar = document.getElementById("snackbar-container")
      var message = document.getElementById("snackbar-message")
  
      // Hide snackbar
      snackbar.style.display = "none";
  
      // Remove message
      message.innerHTML = ''
    },
    showError(err){
      if('message' in err.response.data){
        this.showSnackbar(err.response.data.message)
      }
    }
  };