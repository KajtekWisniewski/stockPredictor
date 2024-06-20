namespace AuthService.Entities
{
    public class Stock
    {

        public int Id { get; set; }
        public string Ticker { get; set; } = "";
        public string DateOfPrediction { get; set; } = "";  
        public float PredictedReturn { get; set; }
        public int DaysPredicted { get; set; } 
    }
}
