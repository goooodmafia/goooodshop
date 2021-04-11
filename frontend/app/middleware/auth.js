export default ({app, redirect, error}) => {

  // Check if the user is logged i
  const isUserLoggedIn = !!app.$apolloHelpers.getToken()
  if (!isUserLoggedIn) {
    error({
      errorCode: 503,
      message: 'You are not allowed to see this'
    })
    app.$apolloHelpers.onLogout()
    redirect('login')
  }
}

//   const hasToken = !!app.$apolloHelpers.getToken()
//   if (!hasToken) {
//     error({
//       errorCode:503,
//       message:'You are not allowed to see this'
//     })
//     app.$router.push('login')
//   }
// }
