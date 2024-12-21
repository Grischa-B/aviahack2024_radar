import React from 'react';
import {Link} from "react-router-dom";
import { Chart } from "react-google-charts";

function Images(props) {
    return (
        <img className="offer-image"
             src={props.links}
             alt={"pic"}
        />
    );
}
const OfferListElement = (props) => {
    const pieData = [
        ["Тип отзыва", "Число отзывов"],
        ["Претензия", 9],
        ["Предложение", 4],
        ["Благодарность", 2],
    ];
    const pieOptions = {
        title: "Отзывы 20.12.2024",
        colors: ["#e74b5e", "#f5e5a1", "#b3eca0"],
    }
    const lineData = [
        ["day", "Претензии", "Предложения", "Благодарности"],
        ["1", 1900, 400,100],
        ["2", 1170, 460,500],
        ["3", 660, 1120,600],
        ["4", 1030, 540,1100],
    ];

    const lineOptions = {
        title: "Типы отзывов за декабрь",
        curveType: "function",
        legend: { position: "bottom" },
        colors: ["#e74b5e", "#f5e5a1", "#b3eca0"],
    };

    return (
        <div className="pie">
            <Chart
                chartType="PieChart"
                data={pieData}
                options={pieOptions}
                width={"100%"}
                height={"300px"}
            />
            <Chart
                chartType="LineChart"
                width="100%"
                height="100%"
                data={lineData}
                options={lineOptions}
                legendToggle
            />
        </div>
    );
};

export default OfferListElement;