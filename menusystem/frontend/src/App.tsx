import { useEffect, useState } from "react";

interface Category {
  id: number;
  name: string;
  placementId: number;
  products: Product[];
}

interface Product {
  id: number;
  name: string;
  image: string;
  description: string;
  price: number;
}


function App() {
  const [categorys, setCategorys] = useState<Category[]>([])
  const handleRequest = async() => {
    const res = await fetch("http://localhost:8000/api/category/");
    setCategorys(await res.json())
    categorys.sort((a, b) => a.placementId - b.placementId);
  }
  useEffect( () => {
    handleRequest()
  }, [])
  return (
    <div className="bg-sky-100" >
      {categorys.map((category) => {
        return (
        <div className="flex justify-center items-center text-center" key={category.id}>
          <div className="block p-6 rounded-lg shadow-lg bg-white max-w-sm w-screen mb-2">
            <h1 className="text-gray-900 text-3xl leading-tight font-[700] mb-2">{category.name}</h1>
                {category.products.map((product) => {
                  return (
                      <ul className="flex justify-between text-left" key={product.id}>
                        <li className="inline-block">
                          <span className="font-xl font-[600] text-xl block">{product.name}</span>
                          <span> {product.description}</span>
                        </li>
                        <li className="font-[600] text-xl mb-2">
                          <span>...{product.price}TL</span>
                        </li>
                      </ul>
                  );
                })}
          </div>
        </div>
      )})}
    </div>
  );
}

export default App;
