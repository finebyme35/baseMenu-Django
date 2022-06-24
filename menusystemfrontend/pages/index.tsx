import type { InferGetServerSidePropsType } from "next";

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
export async function getServerSideProps() {
  const res = await fetch("http://localhost:8000/api/category/");
  const categorys: Category[] = await res.json();
  categorys.sort((a, b) => a.placementId - b.placementId);
  return {
    props: { categorys }, // will be passed to the page component as props
  };
}

function Home({
  categorys,
}: InferGetServerSidePropsType<typeof getServerSideProps>) {
  return (
    <>
      {categorys.map((category) => {
        return (
        <div className="grid grid-cols-1 gap-4 place-items-center" key={category.id}>
          <div className="pt-8 text-left w-full">
            <div className="rounded overflow-hidden shadow-lg mb-5">
              <div className="font-bold text-3xl mb-2 text-center">
                {category.name}
              </div>
              <div className="px-6 py-4">
                {category.products.map((product) => {
                  return (
                      <ul className="flex justify-between items-center" key={product.id}>
                        <li className="inline-block">
                          <span className="font-bold text-xl block">{product.name}</span>
                          <span> {product.description}</span>
                        </li>
                        <li className="font-bold text-xl mb-2">
                          ...{product.price}TL
                        </li>
                      </ul>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      )})}
    </>
  );
}

export default Home;
