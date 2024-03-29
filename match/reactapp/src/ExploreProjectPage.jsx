import "bootstrap/dist/css/bootstrap.min.css";
import Header from "./components/Header";
import ListCard from "./components/ListCard";
import sidebanner from "./components/icons/sidebanner.png";
import VerticalList from "./components/VerticalList";
import ProjectHeaderContent from "./components/ProjectHeaderContent";
import groupprofile from "./components/icons/groupprofile.jpg";
import ashesibanner from "./components/icons/campusbanner.png";
import HorizontalList from "./components/HorizontalList";
import SubListCard from "./components/SubListCard";
import Notification from "./components/Notification";
import IconItem from "./components/IconItem";
import clockicon from "./components/icons/clockicon.png";
import React, { useState } from "react";

const ExploreProjectPage = () => {
  const [applicationStatus, setApplicationStatus] = useState("pending");
  const workhours = 40;
  const appsElement =
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus eros eu vehicula interdum. Cras nec ultricies massa. Curabitur rutrum, diam id consequat consequat";

  const appscontent = [appsElement, appsElement, appsElement];

  const milestoneElement =
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus eros eu vehicula interdum. Cras nec ultricies massa. Curabitur rutrum, diam id consequat consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus eros eu vehicula interdum. Cras nec ultricies massa. Curabitur rutrum, diam id consequat consequat";

  const milestonecontent = [
    milestoneElement,
    milestoneElement,
    milestoneElement,
  ];

  const commentElement = (
    <Notification
      title={"Itachi Uchiha"}
      text={
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus eros eu vehicula interdum. Cras nec ultricies massa. Curabitur rutrum, diam id consequat consequat"
      }
      date={"11:23 - Aug 2023"}
    />
  );

  const handleApplyClick = () => {
    // Toggle between "Apply" and "Pending" when the button is clicked
    setApplicationStatus((prevStatus) =>
      prevStatus === "pending" ? "applied" : "pending"
    );
    // Additional logic can be added here, such as making an API call to submit the application
  };

  const commentcontent = [commentElement, commentElement, commentElement];

  const notificationElement = (
    <Notification
      title={"Onedrive Library"}
      text={
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus eros eu vehicula interdum. Cras nec ultricies massa. Curabitur rutrum, diam id consequat consequat"
      }
      date={"11:23 - Aug 2023"}
    />
  );

  const notificationcontent = [
    notificationElement,
    notificationElement,
    notificationElement,
  ];

  return (
    <div>
      <Header
        Page={
          <HorizontalList
            spacing={20}
            items={[
              <VerticalList
                spacing={20}
                items={[
                  <ProjectHeaderContent
                    title={
                      <VerticalList
                        items={[
                          <div
                            style={{
                              marginTop: "20px",
                              fontWeight:"500"
                            }}
                          >
                            {"Research Associate"}
                          </div>,
                          <div
                            style={{
                              display: "flex",
                              justifyContent: "space-between",
                            }}
                          >
                            <div style={{ maxWidth: "90%", fontSize: "20px" }}>
                              {
                                "Ghana Economic Index Study for people with special abilities "
                              }
                            </div>
                            <button
                              style={{
                                border: "none",
                                borderRadius: "5px",
                                width: "100px",
                                marginRight: "10px",
                                padding: "5px 10px",
                                fontWeight: "600",
                                backgroundColor: "#AD3537",
                                color: "white",
                                textDecoration: "none" /* Remove underline */,
                                fontSize: "18px",
                                marginTop: "-20px",
                                height:"40px"
                              }}
                              onClick={handleApplyClick}
                            >
                              {applicationStatus === "applied"
                                ? "Applied"
                                : "Apply"}
                            </button>
                          </div>,
                        ]}
                      />
                    }
                    const
                    TimeLeft={
                      <HorizontalList
                        spacing={20}
                        items={[
                          <div>{"1yr 3months"}</div>,
                          <div
                            style={{
                              color: "#0A66C2",
                            }}
                          >
                            <IconItem
                              icon={clockicon}
                              item={`${workhours}hrs/wk`}
                            />
                          </div>,
                        ]}
                      />
                    }
                    Duration={"Aug 2023 - Jun 2024"}
                    Description={
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibuseros eu vicula interdum.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibuseros eu vehicula interdum."
                    }
                    profile={groupprofile}
                    People={["Clark Kent", "Superman", "Naruto Uzumaki"]}
                    Date={"12 Aug 2023"}
                    banner={ashesibanner}
                  />,

                  <ListCard
                    items={milestonecontent}
                    title={"Responsibility"}
                    NoItemMessage={"You have no milestones"}
                  />,
                  <ListCard
                    items={appscontent}
                    title={"Requirements"}
                    NoItemMessage={"You have no Apps"}
                  />,
                ]}
              />,

              <VerticalList
                spacing={20}
                items={[
                  <img
                    src={sidebanner}
                    alt=""
                    style={{
                      width: "25vw",
                      paddingLeft: "20px",
                      paddingRight: "20px",
                      backgroundColor: "white",
                      borderRadius: "10px",
                    }}
                  />,
                  <SubListCard
                    items={notificationcontent}
                    title={"Notifications (3)"}
                    NoItemMessage={"You have no notifications"}
                  />,
                ]}
              />,
            ]}
          />
        }
      />
    </div>
  );
};

export default ExploreProjectPage;
