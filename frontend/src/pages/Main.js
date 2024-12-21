import React, {useEffect, useState} from 'react';
import StatChart from "../components/StatChart";




const Main = () => {
    const [adsInfo, setAdsInfo] = useState([])
    const [searchType, setSearchType] = useState("housing")
    return (
        <div>
            <p className="description"></p>
            <StatChart name={"blah"} />
        </div>
    );
};

export default Main;