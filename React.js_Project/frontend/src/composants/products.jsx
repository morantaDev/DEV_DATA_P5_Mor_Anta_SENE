import { useEffect, useState } from "react";
import axios from 'axios';



// const Buttons = ({onClick}) => {
//     return(
//     <div className="text-center my-12">
//         <button className="rounded-lg bg-lime-400 mx-4 px-8 py-1" onClick={onclick}>Prev</button>
//         <button className="rounded-lg bg-lime-400 mx-4 px-8 py-1" onClick={onclick}>Next</button>
//     </div>
//     )
// }
const Product = () => {
    const [datas, setDatas] = useState([]);
    const [Hover, setHovered] = useState([null]);
    const [startValue, setStartValue] = useState(0);
    const [endValue, setEndValue] = useState(15);


    useEffect(() => {
        const fetchData = async() => {
            try{
                const response = await axios.get("http://localhost:5000/products/");
                setDatas(response.data)
    
            }catch(error){
                console.error("Error fetching data:", error);
            }
        }
        fetchData();
    }, []);
    console.log(datas);

    const handleMouseEnter = (product) => {
        setHovered(product)
    }

    const handleMouseLeave = () => {
        setHovered(null)
    }

    const handlePaginationIncrement = () => {
        setStartValue((prevStart) => prevStart + 15);
        setEndValue((prevEnd) => prevEnd + 15);
    }
    const handlePaginationDecrement = () => {
        setStartValue((prevStart) => (prevStart !== 0 ? prevStart - 15 : prevStart));
        setEndValue((prevEnd) => (prevEnd - 15 >= 15 ? prevEnd -15 : prevEnd));
    }

    const  DisplayDetails = () => {
        return(
            <p className="py-2 text-center z-50 delay-300 -translate-y-10 bg-white duration-200 underline">Découvrir les détails</p>
        )
    }
    return (
        <div>
            <div className="flex flex-wrap ml-52 my-8">
              {datas.slice(startValue, endValue).map((product) => (
                <div key={product.id} className="hover:shadow-xl rounded-lg w-80 h-200 cursor-pointer mx-4 my-2 relative" onMouseEnter={() => handleMouseEnter(product)}  onMouseLeave={handleMouseLeave}>
                    <img src={product.url} alt="ProductImage" />
                    {Hover === product && <DisplayDetails />}
                    <p className="text-center text-lg font-bold">{product.name}</p>
                    <p className="text-center text-sm">à partir de</p>
                    <p className="text-center font-serif font-bold text-lg">{product.price} €</p>
                </div>
                
                ))}
            </div>
            {/* <Buttons /> */}
            <div className="text-center my-12">
                <button className="rounded-lg bg-lime-400 mx-4 px-8 py-1" onClick={handlePaginationDecrement}>Prev</button>
                <button className="rounded-lg bg-lime-400 mx-4 px-8 py-1" onClick={handlePaginationIncrement}>Next</button>
            </div>
        </div>
      );
}

export default Product;
