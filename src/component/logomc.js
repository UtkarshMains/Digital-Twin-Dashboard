import React, { useState, useEffect } from "react";
import demand from "../db.json";
import fixed from "../fixed_cost.json";
import freight from "../freight.json";
import capacity from "../capacity.json";
import varc from "../vc.json";
import "./logomc.css";
import "./data.css";
import stage1 from "../image/stage1.png";
import stage3 from "../image/stage3.png";
import stage4 from "../image/stages.png";
import stage5 from "../image/stage5.png";
import stage6 from "../image/stage6.png";
import totalcost from "../image/totalcost.png"
import stage7 from "../image/stage7.png";
import vc from "../image/vc.png"

// Replace this with the correct path to your PieChart.js component

function Logomc() {
  const [countrys, setCountrys] = useState(demand);
  const [caps, setCaps] = useState(capacity);
  const [varcs, setVarcs] = useState(varc);
  const [fcs, setFcs] = useState(fixed);
  const [frcs, setFrcs] = useState(freight);
  const [data, setData] = useState([{}]);
  const [buttonClicked1, setButtonClicked1] = useState(false);
  const [buttonClickedr, setButtonClickedr] = useState(false);
  const [count, setCount] = useState(0);
  const [isShown1,setIsShown1]=useState(false);
  const [isShown3,setIsShown3]=useState(false);
  const [isShown4,setIsShown4]=useState(false);
  const [isShown5,setIsShown5]=useState(false);
  const [isShown6,setIsShown6]=useState(false);
  const [isShown7,setIsShown7]=useState(false);
  const [isShowntc,setIsShowntc]=useState(false);
  const [isShownvc,setIsShownvc]=useState(false);
  useEffect(() => {
    if (buttonClicked1) {
      fetch("/mona")
        .then((res) => res.json())
        .then((data) => {
          setData(data);
          console.log(data);
        });
        setButtonClicked1(false);
    }
  }, [buttonClicked1]);

  const handleButtonClick = () => {
    setButtonClicked1(true);
  };
  const handleButtonClickvc = () => {
    setIsShown1(false);
    setIsShown3(false);
    setIsShown4(false);
    setIsShown5(false);
    setIsShown6(false);
    setIsShown7(false);
    setIsShowntc(false);
    setIsShownvc(true);
  };
  const handleButtonClick1 = () => {
    setIsShown1(true);
    setIsShown3(false);
    setIsShown4(false);
    setIsShown5(false);
    setIsShown6(false);
    setIsShown7(false);
    setIsShowntc(false);
    setIsShownvc(false);
  };

  const handleButtonClick3 = () => {
    setIsShown1(false);
    setIsShown3(true);
    setIsShown4(false);
    setIsShown5(false);
    setIsShown6(false);
    setIsShown7(false);
    setIsShowntc(false);
    setIsShownvc(false);
  };

  const handleButtonClick4 = () => {
    setIsShown1(false);
    setIsShown3(false);
    setIsShown4(true);
    setIsShown5(false);
    setIsShown6(false);
    setIsShown7(false);
    setIsShowntc(false);
    setIsShownvc(false);
  };

  const handleButtonClick5 = () => {
    setIsShown1(false);
    setIsShown3(false);
    setIsShown4(false);
    setIsShown5(true);
    setIsShown6(false);
    setIsShown7(false);
    setIsShowntc(false);
    setIsShownvc(false);
  };


  const handleButtonClick6 = () => {
    setIsShown1(false);
    setIsShown3(false);
    setIsShown4(false);
    setIsShown5(false);
    setIsShowntc(false);
    setIsShown6(true);
    setIsShown7(false);
    setIsShownvc(false);
  };


  const handleButtonClick7 = () => {
    setIsShown1(false);
    setIsShown3(false);
    setIsShown4(false);
    setIsShown5(false);
    setIsShown6(false);
    setIsShown7(true);
    setIsShowntc(false);
    setIsShownvc(false);
  };
  const handleButtonClicktc = () => {
    setIsShown1(false);
    setIsShown3(false);
    setIsShown4(false);
    setIsShown5(false);
    setIsShown6(false);
    setIsShown7(false);
    setIsShowntc(true);
    setIsShownvc(false);
  };
  useEffect(() => {
    if (buttonClickedr) {
      fetch("/reseta")
        .then((res) => res.json())
        .then((data) => {
          setData(data);
          console.log(data);
        });
        setButtonClickedr(false);
    }
  }, [buttonClickedr]);

  const handleButtonClickr = () => {
    setButtonClickedr(true);
    setIsShown1(false);
    setIsShown3(false);
    setIsShown4(false);
    setIsShown5(false);
    setIsShown6(false);
    setIsShown7(false);
  };
  return (
    <div>
      <h2 className="head">Monte Carlo Simulation</h2>
      <div className="dtop">
        <div className="dash">
        {isShownvc &&(
        <div>
        
          <h4>Factory + Freight Variable Costs</h4>
          
          
          <div className="img">
          <img src={vc}></img>
          </div>
        </div>
        )}
        {isShown1 &&(
        <div>
        
          <h4>stage 1</h4>
          
          
          <div className="img">
          <img src={stage1}></img>
          </div>
        </div>
        )}
        {isShown3 &&(
        <div>
          <h4>Stage 2</h4>
          
          
          <div className="img">
          <img src={stage4}></img>
          </div>
        </div>
        )}
        {isShown4 &&(
        <div>
          <h4>Stage 3</h4>
          
  
          <div className="img">
          <img src={stage3}></img>
          </div>
        </div>
        )}
        {isShown5 &&(
        <div>
          <h4>Stage 4</h4>
          
         
          <div className="img">
          <img src={stage5}></img>
          </div>
        </div>
        )}
        {isShown6 &&(
        <div>
          <h4>Stage 5</h4>
          
         
          <div className="img">
          <img src={stage6}></img>
          </div>
        </div>
        )}
        {isShown7 &&(
        <div>
          <h4>Stage 6</h4>
          
          
          <div className="img">
          <img src={stage7}></img>
          </div>
          
        </div>
        )}
        {isShowntc &&(
        <div>
        
          <h4>Optimal Cost for each Scenario</h4>
          
          
          <div className="img">
          <img src={totalcost}></img>
          </div>
        </div>
        )}
        </div>
        <button onClick={handleButtonClick} className="start">Simulate</button>
        <button onClick={handleButtonClickvc} className="start">Factory + Freight Variable Costs</button>
        <button onClick={handleButtonClick1} className="start">Stage 1</button>
        <button onClick={handleButtonClick3} className="start">Stage 2</button>
        <button onClick={handleButtonClick4} className="start">Stage 3</button>
        <button onClick={handleButtonClick5} className="start">Stage 4</button>
        <button onClick={handleButtonClick6} className="start">Stage 5</button>
        <button onClick={handleButtonClick7} className="start">Stage 6</button>
        <button onClick={handleButtonClicktc} className="start">Optimal Cost for each Scenario</button>
        <button onClick={handleButtonClickr} className="start">reset</button>
      </div>
      <h4 className="datah">DataSet</h4>
      <div className="dataset">
        <div>
          <h4>Demand by Market</h4>
          <table className="demandt">
            <thead>
              <th>Country</th>
              <th>Demand</th>
            </thead>
            <tbody>
              {countrys.map((country) => (
                <tr>
                  <td>{country.Country}</td>
                  <td>{country.Demand}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        
        <div>
          <h4>Plants Capacity</h4>
          <table className="demandt">
            <thead>
              <th>Capacity kUnits/month</th>
              <th>LOW</th>
              <th>HIGH</th>
            </thead>
            <tbody>
              {caps.map((cap) => (
                <tr>
                  <td>{cap.Capacity}</td>
                  <td>{cap.LOW}</td>
                  <td>{cap.HIGH}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div>
          <h4>Cost for plant setup</h4>
          <table className="demandt">
            <thead>
              <th></th>
              <th>LOW</th>
              <th>HIGH</th>
            </thead>
            <tbody>
              {fcs.map((fc) => (
                <tr>
                  <td>{fc.Country}</td>
                  <td>{fc.LOW}</td>
                  <td>{fc.HIGH}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>


        <div>
          <h4>Shipping Cost</h4>
          <table className="demandt">
            <thead>
              <th>Freight Costs</th>
              <th>USA</th>
              <th>GERMANY</th>
              <th>JAPAN</th>
              <th>BRAZIL</th>
              <th>INDIA</th>
            </thead>
            <tbody>
              {frcs.map((frc) => (
                <tr>
                  <td>{frc.Freight}</td>
                  <td>{frc.USA}</td>
                  <td>{frc.GERMANY}</td>
                  <td>{frc.JAPAN}</td>
                  <td>{frc.BRAZIL}</td>
                  <td>{frc.INDIA}</td>

                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
      <div>
          <h4>Manufacturing variable costs</h4>
          <table className="demandt">
            <thead>
              <th>Variable Costs</th>
              <th>USA</th>
              <th>GERMANY</th>
              <th>JAPAN</th>
              <th>BRAZIL</th>
              <th>INDIA</th>
            </thead>
            <tbody>
              {varcs.map((mvc) => (
                <tr>
                  <td>{mvc.Variable_Costs}</td>
                  <td>{mvc.USA}</td>
                  <td>{mvc.GERMANY}</td>
                  <td>{mvc.JAPAN}</td>
                  <td>{mvc.BRAZIL}</td>
                  <td>{mvc.INDIA}</td>

                </tr>
              ))}
            </tbody>
          </table>
        </div>
    </div>
  );
}
export default Logomc;
