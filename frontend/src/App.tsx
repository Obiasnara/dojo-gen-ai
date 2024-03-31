import React, { useState } from "react"

import AudioReactRecorder, { RecordState } from "audio-react-recorder"
import { Streamlit } from "streamlit-component-lib"

export const App = () => {
  const [recordState, setRecordState] = useState(null)
  const [urlState, setUrlState] = useState(String)

  const onStop = ({ blob, url }: { blob: Blob; url: string }) => {
    // sauvegarder l'url pour pouvoir ré-écouter l'enregistrement
    setUrlState(url)
    blob.arrayBuffer().then((blobData) =>{
      const blobArray = new Uint8Array(blobData)
      Streamlit.setComponentValue({ "arr": blobArray })
    })
 
		// envoyer le contenu du fichier au back pour pouvoir le manipuler par la suite
  }

  return ( 
   <div>Ready to build your AI note taker ? Let's go 🚀🔥
      <AudioReactRecorder state={recordState} onStop={onStop}/>
      <button onClick={()=>{recordState == RecordState.START ? setRecordState(RecordState.STOP) : setRecordState(RecordState.START)}}>
          {recordState == RecordState.START ? "Stoper" : "Commencer"}
      </button>
      <audio id="audio" controls src={urlState} />
   </div>
  )
}
