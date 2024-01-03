import React, { useState, useEffect } from "react";
import axios from "axios";
import HorizontalList from "./components/HorizontalList";
import VerticalList from "./components/VerticalList";
import HomeHeader from "./components/HomeHeader";
import Header from "./Header";
import SubListCard from "./components/SubListCard";
import addicon from "./components/icons/addicon.png";
import ProjectCardList from "./components/ProjectCardList";
import Notification from "./components/Notification";
import { Link } from "react-router-dom";
import NotificationsList from "./components/NotificationsList";
import SubBanner from "./components/SubBanner";
import ProjectCard from "./components/ProjectCard";
import { useAuth } from "./AuthContext";
import { AuthProvider } from "./AuthContext";
import { useNavigate } from "react-router-dom";
import sidebanner from "./components/icons/sidebanner.png";



const HomePage = () => {


    const [projects, setData] = useState([]);

    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch(
            "http://127.0.0.1:8000/ra/get_all_projects/"
          );
          const result = await response.json();
          setData(result);
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      };

      fetchData();
    }, []);

  const notificationElement = (
    <Notification
      key="notification"
      title={"Onedrive Library"}
      text={
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus eros eu vehicula interdum. Cras nec ultricies massa. Curabitur rutrum, diam id consequat consequat"
      }
      date={"11:23 - Aug 2023"}
    />
  );

  const notificationContent = Array(3).fill(notificationElement);

  const createproject = (
    <Link
      to="/createproject"
      style={{
        width: "420px",
        maxHeight: "174px",
        backgroundColor: "white",
        borderRadius: "15px",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        key="createProject"
        style={{
          width: "420px",
          minHeight: "174px",
          backgroundColor: "white",
          borderRadius: "15px",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <VerticalList
          spacing={10}
          items={[
            <div
              key="createProjectText"
              style={{
                marginTop: "20px",
                fontSize: "30px",
                fontWeight: "600",
                color: "#CAC9CD",
              }}
            >
              Create New Project
            </div>,
            <img
              key="addIcon"
              src={addicon}
              alt=""
              style={{
                width: "40px",
                marginLeft: "110px",
              }}
            />,
          ]}
        />
      </div>
    </Link>
  );
;

  const [dataList, setDataList] = useState([
    { id: 1, title: "Item 1", milestone: "milestone 1" },
    { id: 2, title: "Item 2", milestone: "milestone 2" },
    { id: 3, title: "Item 3", milestone: "milestone 3" },
  ]);

  const cards =
    projects &&
      projects.map((item, index) => (
        <ProjectCard
          key={item.id}
          title={item.title}
          dueDate={"22 Aug 2023"}
          progress={16}
          milestone={"milestone 3"}
          timeleft={"2wks"}
        />
      ))
  ;
  return (
    <div>
      <Header
        Page={[
          <div key="mainContent">
            <HorizontalList
              spacing={20}
              items={[
                <div key="leftContent">
                  <VerticalList
                    spacing={20}
                    items={[
                      <HomeHeader
                        key="homeHeader"
                        title={"My Projects"}
                        date={"22 Aug 2023"}
                        spacing={"30vw"}
                      />,
                      <ProjectCardList cards={cards} />,
                    ]}
                  />
                </div>,
                <div>
                  <VerticalList
                    key="rightContent"
                    spacing={20}
                    items={[
                      <div>
                        <VerticalList
                          key="rightContent"
                          spacing={20}
                          items={[
                            <SubBanner />,
                            <SubListCard
                              // key="subListCard"
                              items={notificationContent}
                              title={"Notifications (3)"}
                              NoItemMessage={"You have no notifications"}
                            />,
                          ]}
                        />
                      </div>,
                    ]}
                  />
                </div>,
              ]}
            />
          </div>,
        ]}
      />
    </div>
  );
};

export default HomePage;