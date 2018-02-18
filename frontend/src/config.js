var BASE_URL = "http://localhost:8000"

if (process.env.NODE_ENV === 'production') {
  BASE_URL = "http://192.168.0.199:8080/" 
}

export default BASE_URL