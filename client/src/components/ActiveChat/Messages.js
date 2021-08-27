import React from "react";
import { Box , Avatar} from "@material-ui/core";
import { SenderBubble, OtherUserBubble } from "../ActiveChat";
import moment from "moment";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(() => ({
  avatar: {
    height: 25,
    width: 25,
    marginTop: "1%",
    marginLeft: "96%",
   
  }
}));

const Messages = (props) => {
  const classes = useStyles();
  const { messages, otherUser, userId} = props;
  return (
    <Box >
      {messages.map((message) => {
        const time = moment(message.createdAt).format("h:mm");

        return message.senderId === userId ? (
          <>
            <SenderBubble key={message.id} text={message.text} time={time} />
            { message === messages[messages.length-1] && 
              message.seen !== null && 
              message.senderId ===  userId &&
              <Avatar alt={otherUser.username} src={otherUser.photoUrl} 
              className={classes.avatar} />}
          </>
        ) : (
          <OtherUserBubble key={message.id} text={message.text} time={time} otherUser={otherUser}  />
        );
      })}
    </Box>
  );
};

export default Messages;
