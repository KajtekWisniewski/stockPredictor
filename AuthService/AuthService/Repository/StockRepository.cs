
using AutoMapper;
using AutoMapper.QueryableExtensions;
using Microsoft.EntityFrameworkCore;
using AuthService.Data;
using AuthService.DTOs;
using AuthService.Entities;
using AuthService.Repository.Contracts;

namespace AuthService.Repository
{
    public class StockRepository(ApplicationDbContext context, IMapper mapper) : IStockRepository
    {
        public void Add(Stock stock)
        {
            context.Stocks.Add(stock);
        }
        public void Delete(Stock stock)
        {
            context.Stocks.Remove(stock);
        }

        public async Task<IEnumerable<T>> GetAll<T>()
        {
            return await context
                .Stocks
                .ProjectTo<T>(mapper.ConfigurationProvider)
                .ToListAsync();
        }

        public async Task<Stock?> GetById(int id)
        {
            return await context.Stocks.FindAsync(id);
        }
        public async Task<T?> GetById<T>(int id)
        {
            return await context
                .Stocks
                .Where(p => p.Id == id)
                .ProjectTo<T>(mapper.ConfigurationProvider)
                .SingleOrDefaultAsync();
        }

        public async Task<bool> SafeChangesAsync()
        {
            return await context.SaveChangesAsync() > 0;
        }


    }
}
