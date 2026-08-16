import { useState } from "react";
import "./App.css";


function App() {


  const [barcode, setBarcode] = useState("");

  const [product, setProduct] = useState(null);

  const [loading, setLoading] = useState(false);



  const searchProduct = async () => {


    if (!barcode) {

      alert("Enter barcode");

      return;

    }


    setLoading(true);


    try {


      const response = await fetch(

        `http://127.0.0.1:8000/product/${barcode}`

      );


      const data = await response.json();


      console.log(data);


      setProduct(data);


    }

    catch(error){


      console.log(error);

      alert("Backend not connected");


    }


    setLoading(false);


  };




  return (

    <div className="container">


      <h1>
        🌱 EcoScan AI
      </h1>


      <p className="subtitle">
        AI powered sustainability and health analyzer
      </p>



      <div className="search">


        <input

          type="text"

          placeholder="Enter barcode"

          value={barcode}

          onChange={(e)=>setBarcode(e.target.value)}

        />


        <button onClick={searchProduct}>

          Scan

        </button>


      </div>



      {

        loading &&

        <h3>
          Analysing product...
        </h3>

      }





      {

        product && product.name &&

        <div className="card">


          <h2>
            {product.name}
          </h2>


          <p>
            Barcode: {product.barcode}
          </p>



          <div className="scores">


            <div>

              🌍

              <h3>
                Eco Score
              </h3>

              <b>
                {product.eco_score}/100
              </b>


            </div>




            <div>

              ❤️

              <h3>
                Health Score
              </h3>


              <b>
                {product.health_score}/100
              </b>


            </div>


          </div>




          <h3>
            Recommendation
          </h3>


          <p>
            {product.recommendation}
          </p>





          <h3>
            Gemini AI Analysis
          </h3>


          <p>
            {product.ai_explanation}
          </p>





          <h3>
            Better Alternatives
          </h3>




          {

            product.alternatives &&

            product.alternatives.map((item,index)=>(


              <div 
                className="alternative"
                key={index}
              >


                <h4>
                  🌱 {item.name}
                </h4>


                <p>
                  Category: {item.category}
                </p>


                <p>
                  Price: ₹{item.price}
                </p>


              </div>


            ))

          }



        </div>


      }


    </div>

  );


}



export default App;