import React from 'react'
import * as navbars from '../components/navbar'
import * as footer from '../components/footer'

export  function Base1({children}) {
  return (
    <div>
        <navbars.Navbar1></navbars.Navbar1>
        <main>
         {children}
        </main>
       
        <footer.Footer1></footer.Footer1>
    </div>
  )
}

