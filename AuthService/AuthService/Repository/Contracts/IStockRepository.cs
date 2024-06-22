using AuthService.Entities;

namespace AuthService.Repository.Contracts
{
    public interface IStockRepository
    {
        Task<IEnumerable<T>> GetAll<T>();
        Task<Stock> GetById(int id);
        Task<T?> GetById<T>(int id);
        void Add(Stock stock);
        void Delete(Stock stock);
        Task<bool> SafeChangesAsync();
    }
}
