import createApiClient from "./api.service";

class PredictService {
    constructor(baseUrl = "/api/detect/") {
        this.api = createApiClient(baseUrl);
    }
    async getAll() {
        const respone = (await this.api.get("/")).data;
        // console.log("service", respone)
        return respone;
    }
    async uploadImage(data) {
        const respone = await this.api.post("/", data);
        console.log(respone.data);
        return respone;
    }
}
export default new PredictService();