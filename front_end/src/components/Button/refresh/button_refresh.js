import React from 'react';
import { Button, Spinner } from 'reactstrap';
import "./button_refresh.css"

function ButtonRefresh ({onclick, status, name}) {
  function getSpinner(){
      return (status ? <Spinner
        size="sm"
        color="secondary"
        className="float-right"/>
        : "")
  }
  function buildBotton() {
    return (
       <Button
       outline
       key={name}
       color="info"
       className={
         status ?
         "button-refresh-resize float-right"
         : "button-refresh-resize fa fa-refresh float-right"}
       onClick={status ? null :onclick} >
         {getSpinner()}
       </Button>
    )
  }
  return buildBotton();
}

export default ButtonRefresh;