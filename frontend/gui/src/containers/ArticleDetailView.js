//import { getKeyThenIncreaseKey } from 'antd/lib/message';
import React from "react";
import CustomForm from "../components/Form";
import axios from "axios";
import { Card } from "antd";

class ArticleDetail extends React.Component {
  state = {
    article: {},
  };
  componentDidMount() {
    const articleID = this.props.match.params.articleID; //I think this takes variable
    //from any part of the root
    axios.get(`http://127.0.0.1:8000/api/${articleID}`).then((res) => {
      this.setState({
        article: res.data,
      });
    });
  }
  render() {
    return (
      <div>
        <Card title={this.state.article.title}>
          <p>{this.state.article.content}</p>
        </Card>
        <br />
        <CustomForm 
        requestType = "put"
        articleID={this.props.match.params.articleID}
        buttonText="Update" />
       </div>
    );
  }
}
export default ArticleDetail;
