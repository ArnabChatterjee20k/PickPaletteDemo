import './App.css'
import { BrowserRouter, Routes , Route } from 'react-router-dom'

import ColorDashboard from "./Page/ColorDashboard"
import Demo from './Page/Demo'
function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<ColorDashboard/>}/>
          <Route path='/demo' element={<Demo/>}/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
