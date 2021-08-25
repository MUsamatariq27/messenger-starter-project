import React from "react";
import { Box, Badge } from "@material-ui/core";
import { BadgeAvatar, ChatContent } from "../Sidebar";
import { makeStyles } from "@material-ui/core/styles";
import { setActiveChat } from "../../store/activeConversation";
import { connect } from "react-redux";
import { readMsgUpdate } from '../../store/utils/thunkCreators';

const useStyles = makeStyles((theme) => ({
  root: {
    borderRadius: 8,
    height: 80,
    boxShadow: "0 2px 10px 0 rgba(88,133,196,0.05)",
    marginBottom: 10,
    display: "flex",
    alignItems: "center",
    "&:hover": {
      cursor: "grab"
    }
  },
  badge: {
    marginRight: 25,
  
  },
  
  
}));

const Chat = (props) => {
  const classes = useStyles();

 const { conversation} = props;
 const { otherUser, messages} = conversation;

  const handleClick = async (conversation) => {
    await props.setActiveChat(conversation.otherUser.username)

    if (messages?.length && !messages[messages.length - 1].seen) {
      await props.updateSeen(conversation.id);
    }
  };

  return (
    <Box onClick={() => handleClick(conversation)} className={classes.root}>
      <BadgeAvatar
        photoUrl={otherUser.photoUrl}
        username={otherUser.username}
        online={otherUser.online}
        sidebar={true}
      />
      <ChatContent conversation={conversation} />

      
      { <Badge badgeContent={messages.filter((msg) => 
      !msg.seen && msg.senderId === otherUser.id)?.length} color="primary" className={classes.badge}/> }
    </Box>
  );
};

const mapDispatchToProps = (dispatch) => {
  return {
    setActiveChat: (id) => {
      dispatch(setActiveChat(id));
    },

    updateSeen: (conversationId) => {
      dispatch(readMsgUpdate(conversationId));
    }

  };
};

export default connect(null, mapDispatchToProps)(Chat);
